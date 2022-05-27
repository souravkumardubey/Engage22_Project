// const searchButton = document.getElementById('search-button');
// const searchInput = document.getElementById('search-input');
// searchButton.addEventListener('click', () => {
//   const inputValue = searchInput.value;
//   alert(inputValue);
// });

document.querySelector('.btn').addEventListener('click',operation);

const movies = [

    {
        title : "Avatar",
        poster : "./img/b14f6e808f23d5284fb5d78a503c6de6.jpeg"
    },
    {
        title : "Avatar2",
        poster : "./img/b14f6e808f23d5284fb5d78a503c6de6.jpeg"
    },
    {
        title : "Avatar3",
        poster : "./img/b14f6e808f23d5284fb5d78a503c6de6.jpeg"
    },
    {
        title : "Jumanji",
        poster : "./img/jumanji-welcome-to-the-jungle_32f61b4a_1_-4MP-framed-296942.webp.crdownload"
    }

]

const parent = document.createElement('div');
parent.className = 'result';
const movie = document.createElement('div');
movie.className = 'movie';
const grandParent = document.querySelector('.result-movie');

const createMovie = (mov) => {
    
    const image_div = document.createElement('div');
    image_div.className = 'poster';
    const movie_img = document.createElement('img');
    movie_img.src = mov.poster;

    image_div.appendChild(movie_img);

    const content = document.createElement('div');
    content.className = 'movie-info';
    
    const movie_title = document.createElement('h3');
    movie_title.className = 'movie-title';
    movie_title.innerHTML = `<span>Title : </span>${mov.title}`;

    movie.appendChild(image_div);
                    
    content.appendChild(movie_title);
    movie.appendChild(content);
    parent.appendChild(movie);
    grandParent.appendChild(parent);
    document.querySelector('.result').style.display = 'block';
    
}

function operation (e) {

    const input = document.getElementById('search').value;
    
    // console.log(input);
    if ( input != null ) {
        
        document.querySelector('.default').style.display = 'none';
        const results = [];
        movies.forEach(element => {
            // console.log(element.title);
            // console.log(element.title);
            // console.log(input);
            if ( element.title.includes(input)) {

                            // console.log(input);  
                // if ( grandParent.hasChildNodes('result') ) {

                //     console.log(grandParent.hasChildNodes('.result'));
                //     grandParent.removeChild(grandParent.lastElementChild);
                //     console.log(grandParent.hasChildNodes());
                    
                // }
                results.push(element);

            }
        
        });

        results.forEach((movie)=> {
            createMovie(movie);
        })

        
        

    }
    e.preventDefault();
}


