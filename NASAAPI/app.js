// fetch ("https://api.nasa.gov/planetary/apod?api_key=tXh04Bb8WZht1s6Mc9uw65cC3XGeGBUSoQmApTb2")
//     .then (res => res.json())
//     .then (data => {
//         console.log(data);
//         document.querySelector("#POD").src = data.url;
//     })
//     .catch (err=> {
//         console.log(`error ${err}`)
//     })

document.querySelector("#getImage").addEventListener("click", getFetch)

async function getFetch() {
    const url = `https://api.nasa.gov/planetary/apod?api_key=tXh04Bb8WZht1s6Mc9uw65cC3XGeGBUSoQmApTb2`
    let data = await fetch (url);
    let imageData = await data.json();
    document.querySelector("#Image").src = imageData.url
    console.log(imageData.url)
}