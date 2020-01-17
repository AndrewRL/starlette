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

  let filterTab = document.getElementById('filters-tab');
  let filterPane = document.getElementById('filter-pane');
  filterTab.onclick = function(e) {
    console.log('Filter tab clicked.');
    console.log(filterTab.innerText);
    if (filterTab.innerText == '+ Options') {
        console.log('In the true case!')
        filterTab.innerText = '- Options';
        filterPane.style.display = 'block';
    } else {
        filterTab.innerText = '+ Options';
        filterPane.style.display = 'none';
    }
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
        console.log(el.href)
        console.log(window.location.href)
        if (el.href == window.location.href) {
            el.style.color = 'crimson';
        } else {
            el.style.color = 'black';
        };
    });
};