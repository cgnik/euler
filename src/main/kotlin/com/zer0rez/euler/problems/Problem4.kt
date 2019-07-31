package com.zer0rez.euler.problems

import com.zer0rez.euler.Problem
import com.zer0rez.euler.Solution
import com.zer0rez.euler.util.isPalindrome

class Problem4 : Problem {
    private data class Product(val product: Int, val x: Int, val y: Int)

    override fun solve(): Solution {
        var products = ArrayList<Product>()
        for (x in 999 downTo 100) {
            for (y in 999 downTo 100) {
                if ((x*y).isPalindrome()) {
                    products.add(Product(x * y, x, y))
                }
            }
        }
        val answer = products.maxBy{it.product}
        return Solution(4, answer?.product.toString(), "${answer?.product} = ${answer?.x} * ${answer?.y}")
    }
}