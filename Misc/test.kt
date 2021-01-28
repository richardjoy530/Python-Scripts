@Entity(tableName = "SignalStrengthRaw")
class SignalStrengthRaw(
    @PrimaryKey @ColumnInfo val time: Long,
    @ColumnInfo(name = "signalStrength") val signalStrength: Int,
    @ColumnInfo(name = "cellularCarrier") val cellularCarrier: String,
    @ColumnInfo(name = "cellularNetworkSpeed") val cellularNetworkSpeed: String
)

@Entity(tableName = "LocationRaw")
class LocationRaw(
    @PrimaryKey @ColumnInfo val collectionTime: Long,
    val locationTime: Long,
    val provider: String,
    val lat: Double,
    val lon: Double,
    val accuracy: Float
)

data class LocationData(var collectedDate: Long) {
    lateinit var carrier: String
    lateinit var networkSpeed: String
    var measurements = ArrayList<GeoHashData>()
}

data class GeoHashData(
    val geoHash: String,
    var avgLatitude: Double,
    var avgLongitude: Double,
    val cellularSignalStrengthQuality: Int,
    var measurementsCount: Int
)

data class LocationSignalData(
    val deviceState: Int,
    val collectionTime: Long,
    val cellularCarrier: String,
    val cellularNetworkSpeed: String,
    val geoHash: String,
    val lat: Double,
    val lon: Double,
)

override fun getAggregate(): ArrayList<LocationData> {
    val locationRawDao = InsightRoomDatabase.getDatabase(context).locationRawDao()
    val signalStrengthDao = InsightRoomDatabase.getDatabase(context).signalStrengthDao()
    val locationRawList = locationRawDao.getByTime(timePeriod.startTime, timePeriod.endTime)
    val signalRawList = signalStrengthDao.getByTime(timePeriod.startTime, timePeriod.endTime)
    return startCooking(locationRawList, signalRawList)
}

private fun startCooking(
    locationRawList: List<LocationRaw>, signalRawList: List<SignalStrengthRaw>
): ArrayList<LocationData> {
    logger.debug("start location cooking")
    val locationDataAggregate = ArrayList<LocationData>()
    val locationSignalDataList = ArrayList<LocationSignalData>()
    for (locationRaw in locationRawList) {
        val signalRaw = getSignalRaw(locationRaw.collectionTime, signalRawList)
        locationSignalDataList.add(
            LocationSignalData(
                1,
                locationRaw.collectionTime,
                signalRaw.cellularCarrier,
                signalRaw.cellularNetworkSpeed,
                GeoHash(locationRaw.lat, locationRaw.lon, 8).toString(),
                locationRaw.lat,
                locationRaw.lon,
                signalRaw.signalStrength
            )
        )
    }

    val groups =
        locationSignalDataList.groupBy { Pair(it.cellularCarrier, it.cellularNetworkSpeed) }
        
    for ((_, value) in groups) {
        for (v in value) {
            //collection date can be same in multiple group, so need to filter carrier and network speed from aggregated list
            val filteredList = locationDataAggregate.filter {
                isSameDate(it.collectedDate, v.collectionTime) &&
                        it.carrier == v.cellularCarrier &&
                        it.networkSpeed == v.cellularNetworkSpeed
            }
            if (filteredList.isEmpty()) {
                //no entry with same date, carrier and network speed
                val locationData = LocationData(v.collectionTime)
                locationData.carrier = v.cellularCarrier
                locationData.networkSpeed = v.cellularNetworkSpeed
                locationData.measurements.add(
                    GeoHashData(v.geoHash, v.lat, v.lon, v.signalStrength, 1)
                )
                locationDataAggregate.add(locationData)
            } else {
                //have entry with same date, carrier and network speed
                aggregateGeoHashData(filteredList.first().measurements, v)
            }
        }
    }
    return locationDataAggregate
}

private fun getSignalRaw(time: Long, signalRaw: List<SignalStrengthRaw>): SignalStrengthRaw {
    //return SignalStrengthRaw wrt the time.
    return signalRaw.dropLastWhile { it.time > time }.last()
}

private fun aggregateGeoHashData(base: ArrayList<GeoHashData>, now: LocationSignalData) {
    val filterList =
        base.filter { it.geoHash == now.geoHash && it.cellularSignalStrengthQuality == now.signalStrength }
    if (filterList.isEmpty()) {
        base.add(GeoHashData(now.geoHash, now.lat, now.lon, now.signalStrength, 1))
    } else {
        val geoHashData = filterList.first()
        geoHashData.avgLatitude = (geoHashData.avgLatitude + now.lat) / 2
        geoHashData.avgLongitude = (geoHashData.avgLongitude + now.lon) / 2
        geoHashData.measurementsCount += 1
    }
}

private fun isSameDate(baseTime: Long, nowTime: Long): Boolean {
    val baseCal = Calendar.getInstance()
    val nowCal = Calendar.getInstance()
    baseCal.timeInMillis = baseTime
    nowCal.timeInMillis = nowTime
    return (baseCal.get(Calendar.DAY_OF_MONTH) == nowCal[Calendar.DAY_OF_MONTH] &&
            baseCal.get(Calendar.MONTH) == nowCal[Calendar.MONTH] &&
            baseCal.get(Calendar.YEAR) == nowCal[Calendar.YEAR])
}