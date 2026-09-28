from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="es">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>Para ti ❤️</title>

    <style>

        * {
            box-sizing: border-box;
        }

        html, body {
            width: 100%;
            height: 100%;
            margin: 0;
        }

        body {

            overflow: hidden;

            font-family:
                "Segoe UI",
                Arial,
                sans-serif;

            background:
                radial-gradient(
                    circle at top,
                    #fff7fb,
                    #ffd9e8,
                    #ffb6d0
                );

            display: flex;
            justify-content: center;
            align-items: center;

            color: #ff4f81;
        }


        /* ==========================================
           FONDO
        ========================================== */

        .fondo-corazones {

            position: fixed;

            inset: 0;

            pointer-events: none;

            overflow: hidden;

            z-index: 0;
        }


        .corazon-flotante {

            position: absolute;

            bottom: -50px;

            font-size: 25px;

            opacity: 0;

            animation:
                subir-corazon
                linear
                infinite;
        }


        @keyframes subir-corazon {

            0% {

                transform:
                    translateY(0)
                    rotate(0deg)
                    scale(0.8);

                opacity: 0;
            }

            10% {
                opacity: 0.7;
            }

            90% {
                opacity: 0.7;
            }

            100% {

                transform:
                    translateY(-110vh)
                    rotate(360deg)
                    scale(1.3);

                opacity: 0;
            }
        }


        /* ==========================================
           CONTENEDOR PRINCIPAL
        ========================================== */

        .contenedor {

            position: relative;

            z-index: 5;

            width: min(90%, 650px);

            text-align: center;

            padding: 30px;

            transition:
                opacity 0.8s ease,
                transform 0.8s ease;
        }


        .desaparecer {

            opacity: 0;

            transform:
                scale(0.8);
        }


        /* ==========================================
           CORAZÓN PRINCIPAL
        ========================================== */

        .corazon-principal {

            font-size: 70px;

            animation:
                latido
                1.2s
                infinite;

            filter:
                drop-shadow(
                    0 8px 15px
                    rgba(255, 70, 130, 0.25)
                );
        }


        @keyframes latido {

            0%, 100% {
                transform: scale(1);
            }

            50% {
                transform: scale(1.15);
            }
        }


        /* ==========================================
           TÍTULOS
        ========================================== */

        h1 {

            font-size:
                clamp(35px, 8vw, 65px);

            margin: 15px 0;

            color: #ff4f81;

            text-shadow:
                0 5px 15px
                rgba(255, 60, 120, 0.2);
        }


        .subtexto {

            font-size:
                clamp(18px, 4vw, 25px);

            color: #ff7199;
        }


        /* ==========================================
           BOTONES
        ========================================== */

        .botones {

            margin-top: 30px;

            display: flex;

            justify-content: center;

            flex-wrap: wrap;

            gap: 15px;
        }


        button {

            border: none;

            padding:
                16px 35px;

            border-radius: 50px;

            font-size: 21px;

            font-weight: bold;

            cursor: pointer;

            transition:
                transform 0.2s,
                box-shadow 0.2s;
        }


        button:hover {

            transform:
                scale(1.1);

            box-shadow:
                0 8px 20px
                rgba(255, 60, 120, 0.25);
        }


        #boton-si {

            background:
                linear-gradient(
                    135deg,
                    #ff4f81,
                    #ff76a2
                );

            color: white;
        }


        #boton-no {

            background: white;

            color: #ff5c8a;
        }


        /* ==========================================
           MENSAJE
        ========================================== */

        .mensaje-grande {

            font-size:
                clamp(30px, 7vw, 55px);

            font-weight: bold;

            color: #ff4f81;

            line-height: 1.2;

            animation:
                aparecer
                1s
                ease;
        }


        .mensaje-pequeno {

            font-size:
                clamp(18px, 4vw, 25px);

            color: #ff7199;

            margin-top: 20px;
        }


        @keyframes aparecer {

            from {

                opacity: 0;

                transform:
                    translateY(20px)
                    scale(0.8);
            }

            to {

                opacity: 1;

                transform:
                    translateY(0)
                    scale(1);
            }
        }


        /* ==========================================
           LIRIO
        ========================================== */

        .flor-contenedor {

            position: relative;

            width: 250px;

            height: 370px;

            margin:
                10px
                auto
                0;

            animation:
                crecer-flor
                2s
                ease
                forwards;

            transform-origin:
                bottom center;
        }


        @keyframes crecer-flor {

            from {

                transform:
                    scaleY(0);

                opacity: 0;
            }

            to {

                transform:
                    scaleY(1);

                opacity: 1;
            }
        }


        /* Tallo */

        .tallo {

            position: absolute;

            width: 13px;

            height: 250px;

            background:
                linear-gradient(
                    to right,
                    #318b42,
                    #61bd69,
                    #318b42
                );

            border-radius: 20px;

            left: 119px;

            top: 105px;

            z-index: 1;
        }


        /* Hojas */

        .hoja {

            position: absolute;

            width: 120px;

            height: 45px;

            background:
                linear-gradient(
                    135deg,
                    #4da957,
                    #78cf75
                );

            border-radius:
                100%
                0
                100%
                0;

            left: 30px;

            top: 245px;

            transform:
                rotate(-25deg);

            z-index: 2;
        }


        .hoja-derecha {

            position: absolute;

            width: 120px;

            height: 45px;

            background:
                linear-gradient(
                    45deg,
                    #4da957,
                    #78cf75
                );

            border-radius:
                0
                100%
                0
                100%;

            left: 100px;

            top: 200px;

            transform:
                rotate(25deg);

            z-index: 2;
        }


        /* ==========================================
           PÉTALOS DEL LIRIO
        ========================================== */

        .flor {

            position: absolute;

            width: 220px;

            height: 180px;

            left: 15px;

            top: 0;

            z-index: 5;
        }


        .petalo {

            position: absolute;

            width: 65px;

            height: 135px;

            left: 78px;

            top: 15px;

            border-radius:
                70%
                70%
                45%
                45%;

            background:
                linear-gradient(
                    to right,
                    #fff,
                    #ffe0ec,
                    #fff
                );

            box-shadow:
                0 5px 15px
                rgba(255, 90, 140, 0.15);

            transform-origin:
                50%
                100%;

            animation:
                abrir-petalo
                1.5s
                ease
                forwards;
        }


        .petalo:nth-child(1) {
            transform:
                rotate(0deg)
                scale(0);
        }

        .petalo:nth-child(2) {
            transform:
                rotate(60deg)
                scale(0);
        }

        .petalo:nth-child(3) {
            transform:
                rotate(120deg)
                scale(0);
        }

        .petalo:nth-child(4) {
            transform:
                rotate(180deg)
                scale(0);
        }

        .petalo:nth-child(5) {
            transform:
                rotate(240deg)
                scale(0);
        }

        .petalo:nth-child(6) {
            transform:
                rotate(300deg)
                scale(0);
        }


        @keyframes abrir-petalo {

            to {

                transform:
                    rotate(var(--rotacion))
                    scale(1);
            }
        }


        .p1 {
            --rotacion: 0deg;
        }

        .p2 {
            --rotacion: 60deg;
        }

        .p3 {
            --rotacion: 120deg;
        }

        .p4 {
            --rotacion: 180deg;
        }

        .p5 {
            --rotacion: 240deg;
        }

        .p6 {
            --rotacion: 300deg;
        }


        /* Centro del lirio */

        .centro-flor {

            position: absolute;

            width: 45px;

            height: 45px;

            border-radius: 50%;

            background:
                radial-gradient(
                    circle,
                    #fff09a,
                    #ffd83d
                );

            left: 87px;

            top: 125px;

            z-index: 20;

            box-shadow:
                0 0 25px
                rgba(255, 215, 60, 0.7);

            animation:
                latido
                1.5s
                infinite;
        }


        /* ==========================================
           PÉTALOS QUE CAEN
        ========================================== */

        .petalos-caida {

            position: fixed;

            inset: 0;

            pointer-events: none;

            overflow: hidden;

            z-index: 10;
        }


        .petalo-caido {

            position: absolute;

            top: -50px;

            font-size: 22px;

            animation:
                caer
                linear
                infinite;
        }


        @keyframes caer {

            0% {

                transform:
                    translateY(0)
                    rotate(0deg);

                opacity: 0;
            }

            10% {
                opacity: 0.9;
            }

            100% {

                transform:
                    translateY(110vh)
                    rotate(540deg);

                opacity: 0;
            }
        }


        /* ==========================================
           RESPONSIVE
        ========================================== */

        @media (max-width: 600px) {

            .contenedor {
                padding: 15px;
            }

            .corazon-principal {
                font-size: 55px;
            }

            button {
                width: 170px;
            }

            .flor-contenedor {
                transform:
                    scale(0.85);
                margin-top: -20px;
            }
        }

    </style>

</head>


<body>


<!-- ============================================
     CORAZONES DEL FONDO
============================================= -->

<div class="fondo-corazones">

    <div class="corazon-flotante"
         style="left:5%; animation-duration:8s; animation-delay:0s;">
        ❤️
    </div>

    <div class="corazon-flotante"
         style="left:15%; animation-duration:11s; animation-delay:2s;">
        💕
    </div>

    <div class="corazon-flotante"
         style="left:30%; animation-duration:9s; animation-delay:1s;">
        💗
    </div>

    <div class="corazon-flotante"
         style="left:45%; animation-duration:13s; animation-delay:4s;">
        ❤️
    </div>

    <div class="corazon-flotante"
         style="left:60%; animation-duration:10s; animation-delay:3s;">
        💕
    </div>

    <div class="corazon-flotante"
         style="left:75%; animation-duration:12s; animation-delay:0s;">
        💗
    </div>

    <div class="corazon-flotante"
         style="left:90%; animation-duration:9s; animation-delay:5s;">
        ❤️
    </div>

</div>


<!-- ============================================
     PÉTALOS
============================================= -->

<div class="petalos-caida" id="petalosCaida"></div>


<!-- ============================================
     CONTENIDO
============================================= -->

<div class="contenedor" id="contenido">

    <div class="corazon-principal">
        ❤️
    </div>

    <h1>
        ¿Me amas unu?
    </h1>

    <div class="subtexto">
        
    </div>


    <div class="botones">

        <button id="boton-si"
                onclick="respuestaSi()">

            Sí 💕
        </button>


        <button id="boton-no"
                onclick="respuestaNo()">

            No 😭
        </button>

    </div>

</div>


<script>


/* ==========================================
   ELEMENTOS
========================================== */

const contenido =
    document.getElementById("contenido");

const petalosCaida =
    document.getElementById("petalosCaida");


/* ==========================================
   RESPUESTA NO
========================================== */

function respuestaNo() {

    contenido.classList.add("desaparecer");


    setTimeout(() => {

        contenido.innerHTML = `

            <div class="corazon-principal">
                🥺
            </div>

            <div class="mensaje-grande">
                unu
            </div>

            <div class="mensaje-pequeno">
                💔
            </div>

        `;

        contenido.classList.remove(
            "desaparecer"
        );

    }, 700);


    setTimeout(() => {

        contenido.classList.add(
            "desaparecer"
        );

    }, 2200);


    setTimeout(() => {

        document.body.innerHTML = "";

    }, 3100);
}


/* ==========================================
   RESPUESTA SÍ
========================================== */

function respuestaSi() {

    contenido.classList.add(
        "desaparecer"
    );


    setTimeout(() => {

        contenido.innerHTML = `

            <div class="corazon-principal">
                ❤️
            </div>

            <div class="mensaje-grande">
                Yo te amo más peque uwu 🥺💕
            </div>

            <div class="mensaje-pequeno">
                Espera un poquito...
            </div>

        `;

        contenido.classList.remove(
            "desaparecer"
        );

    }, 700);


    setTimeout(() => {

        mostrarFlor();

    }, 3000);
}


/* ==========================================
   MOSTRAR LIRIO
========================================== */

function mostrarFlor() {

    contenido.classList.add(
        "desaparecer"
    );


    setTimeout(() => {

        contenido.innerHTML = `

            <div class="flor-contenedor">

                <div class="flor">

                    <div class="petalo p1"></div>
                    <div class="petalo p2"></div>
                    <div class="petalo p3"></div>
                    <div class="petalo p4"></div>
                    <div class="petalo p5"></div>
                    <div class="petalo p6"></div>

                    <div class="centro-flor"></div>

                </div>


                <div class="tallo"></div>

                <div class="hoja"></div>

                <div class="hoja-derecha"></div>

            </div>


            <div
                class="mensaje-grande"
                id="mensajeFinal">
            </div>


            <div class="mensaje-pequeno">
                🌸 Para ti 🌸
            </div>

        `;


        contenido.classList.remove(
            "desaparecer"
        );


        crearPetalos();

        escribirMensaje();


    }, 700);
}


/* ==========================================
   TEXTO ESCRITO
========================================== */

function escribirMensaje() {

    const texto =
        "Te amo muchoooo ❤️";

    const elemento =
        document.getElementById(
            "mensajeFinal"
        );

    let posicion = 0;


    function escribir() {

        if (posicion < texto.length) {

            elemento.innerHTML +=
                texto.charAt(posicion);

            posicion++;

            setTimeout(
                escribir,
                100
            );

        }

    }


    escribir();
}


/* ==========================================
   CREAR PÉTALOS
========================================== */

function crearPetalos() {

    const simbolos = [
        "🌸",
        "🌷",
        "💗",
        "💕",
        "❤️"
    ];


    for (let i = 0; i < 25; i++) {

        const petalo =
            document.createElement("div");


        petalo.className =
            "petalo-caido";


        petalo.innerHTML =
            simbolos[
                Math.floor(
                    Math.random()
                    * simbolos.length
                )
            ];


        petalo.style.left =
            Math.random() * 100 + "%";


        petalo.style.animationDuration =
            (5 + Math.random() * 7) + "s";


        petalo.style.animationDelay =
            Math.random() * 5 + "s";


        petalo.style.fontSize =
            (15 + Math.random() * 20) + "px";


        petalosCaida.appendChild(
            petalo
        );
    }
}


</script>

</body>

</html>
"""


@app.route("/")
def inicio():
    return render_template_string(HTML)


if __name__ == "__main__":

    print()
    print("======================================")
    print("       REGALITO PARA MI AMOR ❤️")
    print("======================================")
    print()
    print("Abre en tu navegador:")
    print("http://127.0.0.1:5000")
    print()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )