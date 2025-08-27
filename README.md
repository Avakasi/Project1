<!doctype html>
<html>
    <head></head>
        <title>Day 1</title>
    <body>
        <canvas id="canv">

        </canvas>
        <script>
            const canvas = document.querySelector("#canv")
            const ctx = canvas.getContext("2d")

            let x = 0
            let vx = 1

            function GameLoop(){
                update()
                draw()
            }
            function update(){
                x += vx
                
                if (x > 215 || x < 0) {
                    vx *= -1
                }
            }

            function draw() {
  
                ctx.fillStyle = "black"
                ctx.beginPath()
                /*ctx.lineTo(0, 0)
                ctx.lineTo(100, 100)
                ctx.lineTo(0, 100)*/
                ctx.rect(0, 0, 215, 150)
                ctx.fill()

                ctx.fillStyle = "white"
                ctx.fillText("1UP", 15, 10)
                ctx.fillText("00", 23, 20)
                ctx.fillText("HIGH SCORE", 70, 10)
                ctx.fillText("16440", 85, 20)

                ctx.fillStyle = "gold"
                ctx.beginPath()
                ctx.arc(x, 100, 5, Math.PI*0., Math.PI*1/1.2)
                ctx.fill()
                
                ctx.fillStyle = "gold"
                ctx.beginPath()
                ctx.arc(x, 100, 5, Math.PI*0., Math.PI*1.28, true)
                ctx.fill()
                requestAnimationFrame(GameLoop)
            }
            /* requestAnimationFrame() takes a function call*/
            /*To loop ^ place at the end of the function + place outside*/
            requestAnimationFrame(GameLoop)
        </script>
    </body>
</html>


