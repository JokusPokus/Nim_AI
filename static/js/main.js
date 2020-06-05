//config paticle js library
particlesJS("particles-js", {
    particles: {
        number: {
            value: 100,
            density: {
                enable: true,
                value_area: 800,
            },
        },
        color: {
            value: "#ffffff",
        },
        shape: {
            type: "circle",
            stroke: {
                width: 0,
                color: "#000000",
            },
            polygon: {
                nb_sides: 5,
            },
            image: {
                src: "img/github.svg",
                width: 100,
                height: 100,
            },
        },
        opacity: {
            value: 0.5,
            random: false,
            anim: {
                enable: false,
                speed: 1,
                opacity_min: 0.1,
                sync: false,
            },
        },
        size: {
            value: 3,
            random: true,
            anim: {
                enable: false,
                speed: 40,
                size_min: 0.1,
                sync: false,
            },
        },
        line_linked: {
            enable: true,
            distance: 150,
            color: "#ffffff",
            opacity: 0.4,
            width: 1,
        },
        move: {
            enable: true,
            speed: 6,
            direction: "none",
            random: false,
            straight: false,
            out_mode: "out",
            bounce: false,
            attract: {
                enable: false,
                rotateX: 600,
                rotateY: 1200,
            },
        },
    },
    interactivity: {
        detect_on: "canvas",
        events: {
            onhover: {
                enable: true,
                mode: "grab",
            },
            onclick: {
                enable: true,
                mode: "push",
            },
            resize: true,
        },
        modes: {
            grab: {
                distance: 140,
                line_linked: {
                    opacity: 1,
                },
            },
            bubble: {
                distance: 400,
                size: 40,
                duration: 2,
                opacity: 8,
                speed: 3,
            },
            repulse: {
                distance: 200,
                duration: 0.4,
            },
            push: {
                particles_nb: 4,
            },
            remove: {
                particles_nb: 2,
            },
        },
    },
    retina_detect: true,
});

/* Preloader function*/
function showPreloader() {
    document.querySelector(".content__container").style.display = "none";
    document.querySelector(".content__btn").style.display = "none";
    document.querySelector(".preload").style.display = "block";
    setTimeout(function () {
        document.querySelector(".preload").style.display = "none";
    }, 10000);
}

/* Validation of coins*/
$(".board-list__check").each(function () {
    $(this).on("click", function () {
        let clickedID = $(this).parents("div .row").attr("id");
        $(".board-list__item").each(function () {
            //if input is checked
            if (
                $(this).parent().attr("id") !== clickedID &&
                $("#board li:has(input:checked)").length !== 0
            ) {
                $(this).parent().css("opacity", "0.2");
                $(this).find("input").attr("disabled", true);
            } else {
                $(this).parent().css("opacity", "1");
                $(this).find("input").attr("disabled", false);
            }
        });
    });
});

/* Number of rounds to train*/
const numberOfRounds = document.querySelector('input[type="range"]');
let newLevelValue;
const rangeValue = function () {
    let newValue;

    if (parseInt(numberOfRounds.value) <= 100) {
        newValue = numberOfRounds.value;
    } else if (parseInt(numberOfRounds.value) <= 200) {
        newValue = (100 + (parseInt(numberOfRounds.value) - 100) * 9).toString();
    } else {
        newValue = (1000 + (parseInt(numberOfRounds.value) - 200) * 90).toString();
    }

    let target = document.querySelector(".value");
    target.innerHTML = newValue;
    let level = document.querySelector(".level");

    if (newValue <= 20) {
        newLevelValue = "EASY PEASY";
        level.classList.remove("level2");
        level.classList.remove("level3");
        level.classList.remove("level4");
        level.classList.remove("level5");
    } else if (newValue <= 100) {
        newLevelValue = "A LIL' CHALLENGE";
        level.classList.remove("level3");
        level.classList.remove("level4");
        level.classList.remove("level5");
        level.classList.add("level2");
    } else if (newValue <= 500) {
        newLevelValue = "KINDA HARD";
        level.classList.remove("level2");
        level.classList.remove("level4");
        level.classList.remove("level5");
        level.classList.add("level3");
    } else if (newValue <= 3000) {
        newLevelValue = "REALLY HARD";
        level.classList.remove("level2");
        level.classList.remove("level3");
        level.classList.remove("level5");
        level.classList.add("level4");
    } else {
        newLevelValue = "PREPARE TO CRY";
        level.classList.remove("level2");
        level.classList.remove("level3");
        level.classList.remove("level4");
        level.classList.add("level5");
    }
    level.innerHTML = newLevelValue;
    return newLevelValue;
};

function showRules() {
    let x = document.getElementById("rules__text");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

numberOfRounds.addEventListener("input", rangeValue);
