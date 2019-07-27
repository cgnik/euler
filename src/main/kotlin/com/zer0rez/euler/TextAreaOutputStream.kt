package com.zer0rez.euler

import javafx.scene.control.TextArea
import java.io.IOException
import java.io.OutputStream

class TextAreaOutputStream(val textArea: TextArea): OutputStream() {

    @Throws(IOException::class)
    override fun write(b: Int) {
        throw UnsupportedOperationException()
    }

    override fun write(b: ByteArray?) {
        super.write(b)
    }

    override fun write(b: ByteArray?, off: Int, len: Int) {
//    override fun write(b: ByteArray?,) {
//        super.write(b)
//    }
//
//    @Throws(IOException::class)
//    override fun write()
        textArea.appendText(b?.toString(Charsets.UTF_8))
        textArea.scrollTop = java.lang.Double.MAX_VALUE
    }

}