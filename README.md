<!doctype html>
<title>Day 1</title>

    </canvas>
    <script>
        const canvas = document.querySelector("#canv")
        const ctx = canvas.getContext("2d")

        class Vector2{
            x
            y
            constructor(x,y){
                this.x = x
                this.y = y
            }
            plusEquals(other){
                this.x += other.x
                this.y += other.y
            }
        }

        let x = 0
        let vx = 1
        let y = 0
        let vy = 1

        let vertex = new Vector2(0,0)
        let velocity = new Vector2(1,1)

        function GameLoop(){
            update()
            draw()
        }
        function update(){
            vertex.plusEquals(velocity)
            
            if (vertex.x > 215 || vertex.x < 0) {
                velocity.x *= -1
            }
            if (vertex.y > canvas.height || vertex.y < 0) {
                velocity.y *= -1
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
            ctx.arc(vertex.x, 100, 5, Math.PI*0., Math.PI*1/1.2)
            ctx.fill()
            
            ctx.fillStyle = "gold"
            ctx.beginPath()
            ctx.arc(vertex.x, 100, 5, Math.PI*0., Math.PI*1.28, true)
            ctx.fill()
            requestAnimationFrame(GameLoop)
        }
        /* requestAnimationFrame() takes a function call*/
        /*To loop ^ place at the end of the function + place outside*/
        requestAnimationFrame(GameLoop)
    </script>
</body>

