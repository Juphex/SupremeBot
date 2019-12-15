function get_items(base_url, initial_url) {
  var Crawler = require("simplecrawler"),
  url = require("url"),
  cheerio = require("cheerio"),
  request = require("request");

  var crawler = new Crawler(initial_url);
  //let items = [];

  request(initial_url, {
      //remember session cookie - optional
      jar: true},
      function(err, response, body) {
          // Start by saving the cookies. We'll likely be assigned a session cookie
          // straight off the bat, and then the server will remember the fact that
          // this session is logged in as user "iamauser" after we've successfully
          // logged in
          //crawler.cookies.addFromHeaders(response.headers["set-cookie"]);

          // We want to get the names and values of all relevant inputs on the page,
          // so that any CSRF tokens or similar things are included in the POST
          // request
          var $ = cheerio.load(body),
                  formDefaults = {},
                  // You should adapt these selectors so that they target the
                  // appropriate form and inputs
                  articles = $("div.inner-article"),
                  a_tags = $("div.inner-article > a"),
                  imgs = $("div.inner-article > a > img");

          articles.each(function(i, article) {
              var link = ($(article["children"]).attr("href"));
              var image = ($(imgs[i]).attr("src"));
              var sold_out = ($(a_tags[i]).children("div.sold_out_tag").text());
              var name = ($(article).children("h1").children("a").text());
              items.push([name, link, image, sold_out]);
              console.log(i);
              //console.log(items[0]);

          });
      }/*,
      function(error, response, body) {
          crawler.start();
      }*/);
  //console.log(items[0]);
  return items;
}


var items = [];

var itemss = get_items("https://www.supremenewyork.com/",
"https://www.supremenewyork.com/shop/all/tops_sweaters");
console.log(itemss.toString());
console.log(items.toString());