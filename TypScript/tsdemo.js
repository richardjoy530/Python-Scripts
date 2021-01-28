"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var like_component_1 = require("./like.component");
var likeComponet = new like_component_1.LikeComponet(15, false);
likeComponet.onClick();
console.log(likeComponet.likeCount);
