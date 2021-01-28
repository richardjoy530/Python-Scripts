"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.LikeComponet = void 0;
var LikeComponet = /** @class */ (function () {
    function LikeComponet(_likeCount, isSelected) {
        this._likeCount = _likeCount;
        this.isSelected = isSelected;
    }
    LikeComponet.prototype.onClick = function () {
        this._likeCount -= (this.isSelected) ? 1 : -1;
        this.isSelected = !this.isSelected;
    };
    Object.defineProperty(LikeComponet.prototype, "likeCount", {
        get: function () {
            return this._likeCount;
        },
        enumerable: false,
        configurable: true
    });
    return LikeComponet;
}());
exports.LikeComponet = LikeComponet;
