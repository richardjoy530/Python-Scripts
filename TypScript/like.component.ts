export class LikeComponet{
    constructor(private _likeCount:number,public isSelected:boolean){
    }

    onClick() {
        this._likeCount -= (this.isSelected)?1:-1
        this.isSelected = !this.isSelected
    }

    get likeCount(){
        return this._likeCount
    }

}