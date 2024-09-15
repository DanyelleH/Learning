fetch('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita')
    .then(res => res.json()) // parse response as JSON
    .then(data => {
      console.log(data.drinks)
      
    })
    .catch(err => {
        console.log(`error ${err}`)
    });
