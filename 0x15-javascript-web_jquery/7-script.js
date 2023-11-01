$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  $('DIV#red_header').text(data.name);
})
