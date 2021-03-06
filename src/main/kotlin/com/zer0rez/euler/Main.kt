import com.zer0rez.euler.Problem
import com.zer0rez.euler.Solution
import javafx.collections.ObservableList
import javafx.geometry.Pos
import javafx.scene.layout.Priority
import org.reflections.Reflections
import tornadofx.*
import java.io.PrintStream
import java.lang.Thread.yield

class ProblemApp : App(ProblemView::class)


class ProblemView : View() {

    lateinit var out: PrintStream

    val controller: Problems by inject()

    override val root = vbox {
        setMinSize(1024.0, 400.0)
        flowpane{
            label("Project Euler Calculator")
            button("Begin Calculation") {
                vboxConstraints { alignment = Pos.CENTER }
                action { controller.solve() }
            }
        }
        tableview(controller.solutions) {
            asyncItems { controller.solutions }
            vboxConstraints { vGrow = Priority.ALWAYS }
            columnResizePolicy = SmartResize.POLICY
            readonlyColumn("Problem", Solution::number)
            readonlyColumn("Answer", Solution::answer)
            readonlyColumn("Extra Info", Solution::extra)
        }
    }
}

class Problems : Controller() {
    var solutions: ObservableList<Solution> = ArrayList<Solution>().observable()
    fun solve() {
        val problems =
            Reflections(Problem::class.java.`package`.name).getSubTypesOf(Problem::class.java).sortedBy { it.name }
        problems.map {
            val t = Thread {
                solutions.add(it.newInstance().solve())
                yield()
            }
            t.start()
            t.join()
        }
    }
}

fun main(args: Array<String>) {
    launch<ProblemApp>(args)
}
