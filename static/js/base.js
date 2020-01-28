window.onload = function() {

  formatTimestamps();
  updateActiveNavLink();

  let searchInput = document.getElementById('search-input');
  let searchButton = document.getElementById('search-button');
  searchInput.oninput = function(e) {
        if (searchInput.value.length > 0) {
            searchButton.style.color = 'crimson';
        } else {
            searchButton.style.color = 'LightGray';
        }
  }

  document.getElementById('search-button').onclick = function(e) {
    console.log('Search button clicked!');
    query = generate_query();
    console.log(query);
    window.location.href = window.location.pathname + query;
  }

  // Color "Posts" nav link when looking at an individual post
  console.log("The function ran on load.");
}


formatTimestamps = function() {
  [...document.querySelectorAll(".timestamp")].map(function(el){
    var utcTime = moment(el.innerText, 'YYYY-M-D H:m:s.S');
    utcTime.local();
    today = moment()
    if (utcTime.isSame(today, 'day')){
        el.innerText = utcTime.fromNow();
    } else if (utcTime.isSame(today, 'year')){
        el.innerText = utcTime.format('MMMM Do');
    } else {
        el.innerText = utcTime.format('MMMM YYYY');
    };
  });
}

updateActiveNavLink = function() {
    [...document.querySelectorAll(".nav-link")].map(function(el) {
        if (el.href == window.location.href) {
            el.style.color = 'crimson';
        } else {
            el.style.color = 'black';
        };
    });
};

generate_query = function() {
    // Get search terms
    let search_terms = document.getElementById('search-input').value
    // Get match-tags button
    let match_tags = document.getElementById('exact-tag-flag').checked
    // Get match all button
    let match_all = document.getElementById('match-all-flag').checked
    // Get exclude tags
    let exclude_tags = document.getElementById('exclude-tags-input').value.replace(/\s/g, "")

    // Build query string
    let query_string = '?search=True&query=' + search_terms

    if (match_tags){
        query_string = query_string + '&match_tags=True';
        search_terms = search_terms.replace(/\s/g, "");
        query_string = query_string + '&tags=' + search_terms
    }

    if (match_all) {
        query_string = query_string + '&match_all=True';
    }

    if (exclude_tags) {
        query_string = query_string + '&exclude=' + exclude_tags
    }

    return query_string
}