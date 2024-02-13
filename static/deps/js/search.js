document.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById('searchForm');
    var searchInput = document.getElementById('searchInput');

    form.addEventListener('submit', function(e) {
      if (searchInput.value.trim() === '') {
        e.preventDefault(); 
        searchInput.placeholder = 'Enter a search query.'; 
        searchInput.classList.add('placeholder-error'); 
      } else {
        searchInput.placeholder = 'Search';
      }
    });
  });