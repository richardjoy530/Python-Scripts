export class Point {
    constructor(private x:number,public y:number){
    }
    draw() {
        console.log("sdf",this.x, this.y)
    }

    get X(){
        return this.x
    }

    set X(value){
        this.x = value
    }
}