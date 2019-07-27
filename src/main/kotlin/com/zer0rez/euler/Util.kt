package com.zer0rez.euler

object Util {
    fun swapin(target : IntArray, arrow: Int){
        target[0] = target[1]
        target[1] = arrow
    }
}