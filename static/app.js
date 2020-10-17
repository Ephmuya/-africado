$(document).ready(function(){
   $('[data-toggle="offcanvas"]').click(function(){
       $("#navigation").toggleClass("hidden-xs");
   });
});


function buildtable(id){
const wrapper = document.getElementById(id);
function fetchData() {
  fetch("./type/"+id)
      .then(data => data.json())
      .then(jsonData => populate(jsonData))
      .catch(e => {
          console.log("Error: " + e)
      });
};
document.addEventListener('DOMContentLoaded', fetchData, false);

function dom(tag, text) {
    let r = document.createElement(tag);
    if (text) r.innerText = text;
    return r;
};
function append(parent, child) {
  parent.appendChild(child);
  return parent;
};

function populate(json) {
    if (json.length === 0) return;
    let keys = Object.keys(json[0]);
    let table = dom('table');
    //header
    append(table,
      keys.map(k => dom('th', k)).reduce(append, dom('tr'))
    );
    //values
    const makeRow = (acc, row) =>
        append(acc,
            keys.map(k => dom('td', row[k])).reduce(append, dom('tr'))
        );
    json.reduce(makeRow, table);
    wrapper.appendChild(table);
};
}

buildtable("major")
buildtable("minor")
buildtable("score")

$("#major_li").click(
function(){
$('.farm-table').addClass('d-none')
$('.major-records').removeClass('d-none')
$('.d_links > li').removeClass('active')
$('#major_li').addClass('active')
}

)

$("#minor_li").click(
function(){
$('.farm-table').addClass('d-none')
$('.minor-records').removeClass('d-none')
$('.d_links > li').removeClass('active')
$('#minor_li').addClass('active')
}

)

$("#score_li").click(
function(){
$('.farm-table').addClass('d-none')
$('.score-records').removeClass('d-none')
$('.d_links > li').removeClass('active')
$('#score_li').addClass('active')
}

)

$('.g-major').click(

function(){
 console.log("yep")
 $('#major tr').find('td').each (function() {
    var cellText = $(this).html();
   if(cellText == 'yes'){
   $(this).text("1");
   }
   else if (cellText == 'no'){
    $(this).text("1");
   }
 else if (cellText == 'na'){
    $(this).text("1");
   }

   else{
       $(this).text("1");
   }
  })
}
)


$('.g-minor').click(

function(){

 $('#minor tr').find('td').each (function() {
    var cellText = $(this).html();
   if(cellText == 'yes'){
   $(this).text("1");
   }
   else if (cellText == 'no'){
    $(this).text("-1");
   }
 else if (cellText == 'na'){
    $(this).text("0");
   }

    else{
    $(this).text("0");
   }
  })
}
)
