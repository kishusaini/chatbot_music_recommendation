
$(document).ready(function () {
    // Fetch top albums data from the server
    $.get("/top_albums", function (data) {
        // Clear existing content
        $(".album-list").empty();

        // Loop through the data and add it to the container
        data.forEach(function (album) {
            var albumCard =
                '<div class="album-card">' +
                '<img src="' + album.image_url + '" alt="' + album.album_name + '" class="album-image">' +
                '<h3 class="album-name">' + album.album_name + '</h3>' +
                '<p class="artist-name">' + album.artist_name + '</p>' +
                '</div>';

            $(".album-list").append(albumCard);
        });
    });
});
