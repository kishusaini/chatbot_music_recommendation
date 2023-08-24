
document.addEventListener("DOMContentLoaded", function() {
    const playButtons = document.querySelectorAll(".play-button");
    const pauseButtons = document.querySelectorAll(".pause-button");
    const audio = new Audio();
    let currentPlayingButton = null;

    playButtons.forEach((button, index) => {
        button.addEventListener("click", () => {
            const audioSrc = button.getAttribute("data-src");
            const card = button.closest(".card");

            if (audioSrc) {
                if (audio.paused || audio.currentTime === 0 || audio.src !== audioSrc) {
                    if (currentPlayingButton !== null) {
                        currentPlayingButton.innerHTML = '<i class="bi bi-play"></i> Play';
                        currentPlayingButton.closest(".card").classList.remove("playing");
                    }
                    audio.src = audioSrc;
                    audio.play();
                    button.innerHTML = '<i class="bi bi-pause"></i>Play';
                    card.classList.add("playing");
                    currentPlayingButton = button;
                } else {
                    audio.pause();
                    button.innerHTML = '<i class="bi bi-play"></i> Play';
                    card.classList.remove("playing");
                }
            }
        });
    });

    pauseButtons.forEach(button => {
        button.addEventListener("click", () => {
            if (!audio.paused) {
                audio.pause();
                const card = button.closest(".card");
                const playButton = card.querySelector(".play-button");
                playButton.innerHTML = '<i class="bi bi-play"></i> Play';
                card.classList.remove("playing");
            }
        });
    });
});
