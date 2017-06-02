function getSlackChannels(event) {
    var value = event.target.value;
    var element = document.getElementById("id_slack_channel");

    if (value) {
        var xhr= new XMLHttpRequest();

        xhr.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                element.innerHTML = '<option value="">---------</option>';
                var channels = JSON.parse(xhr.response)
                for (var i in channels) {
                    element.innerHTML +=
                        '<option value="' + channels[i] + '">' + channels[i] + '</option>';
                }
            }
        };

        xhr.open("POST", "/get_slack_channels/", true);
        xhr.setRequestHeader("Content-Type", "application/json");

        var data = JSON.stringify({
            "team_id": value
        });

        xhr.send(data);
    }
    else {
        element.innerHTML = "";
    }
}

document.addEventListener("DOMContentLoaded", function(event) { 
    document.getElementById("id_team").addEventListener("change", getSlackChannels);
});