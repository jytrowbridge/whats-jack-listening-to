let xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    let [tracks, currentlyPlaying] = JSON.parse(this.responseText)
    console.log(tracks)
    console.log(currentlyPlaying)
  }
};

const updateSongs = () => {
  console.log('testing ajax')
  setInterval(() => {
    xhttp.open("GET", "/test_ajax", true);
    xhttp.send();
  },
  5000)
}
