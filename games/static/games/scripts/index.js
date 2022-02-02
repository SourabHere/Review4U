 //popover
 var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
 var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
     return new bootstrap.Popover(popoverTriggerEl)

 });

 let search = document.getElementById('search1');
 let searchbtn = document.getElementById('searchbtn');


 //updatePopover

 function updatePopover() {
     console.log("we are here");

     var popstr = "";
     let count = 0
     more = document.getElementsByClassName('more');
     Array.from(more).forEach(element => {
         let Gname = element.textContent;

         curclass = document.querySelector(`.G${count}`);
         originnalname = Gname;
         Gname = Gname.toLowerCase();
         // searchval = searchval.toLowerCase();
         // searchsize = searchval.length;

         Gameimg = document.getElementById(`Game${count}`);

         detail=document.getElementById(`detail${count}`);

         // console.log("yahooo");
         // console.log(Aname);


         popstr = popstr + `<div class="card mb-3 cardrecc box${count}" id="cardrecc" style="width:auto;">
             <div class="row g-0 content${count} poparea">
                 <div class="col-md-4 popimgarea">
                     <a href="${detail.getAttribute("href")}" class="linkimg"><img src="${Gameimg.getAttribute("src")}" class="img-fluid rounded-start popimage" alt="..."></a>
                     </div>
                     <div class="col-md-8" id="poptext">
                         <div class="card-body popcbody" >
                             <a href="${detail.getAttribute("href")}" class="more2"><h5 class="card-title card${count} poptitle" >${originnalname}</h5></a>
                             </div>
                             </div>
                             </div>
                             </div>`;
         search.setAttribute('data-bs-content', popstr);

         count++;
     });
     // console.log(popstr);

     search.setAttribute('data-bs-content', popstr);
     // $('#search1').popover('show');
 }



 // let search = document.getElementById('search1');
 // let searchbtn = document.getElementById('searchbtn');

 search.addEventListener("input", function () {
     // let searchval = search.value;
     // console.log(searchval);
     let searchval = search.value.toLowerCase();
     // console.log(searchval);

     updatePopover(searchval);


     if (searchval == '') {
         // console.log("here");
         $('#search1').popover('hide');

     }
     else {
         // console.log("not here");
         $('#search1').popover('show');
     }

     let searchpop = document.getElementsByClassName("cardrecc");
     // console.log(searchpop.textContent);

     let count = 0;
     Array.from(searchpop).forEach(element => {
         // console.log(element.textContent);

         let cardn = document.querySelector(`.card${count}`);
         let box = document.querySelector(`.box${count}`);

         let Gamehere = cardn.textContent;
         Gamehere = Gamehere.toLowerCase();

         // console.log(Animehere);
         // console.log(count);

         if (Gamehere == searchval || Gamehere.slice(0, searchval.length) == searchval) {
             box.style.display = "";
         }
         else {
             box.style.display = "none";
         }

         count++;
     })

 });

 searchbtn.addEventListener("click", function (event) {
     event.preventDefault();
     let finalinp = search.value;
     // console.log(finalinp);

     let count = 0;
     more = document.getElementsByClassName('more');
     Array.from(more).forEach(element => {
         let Gname = element.textContent;

         curclass = document.querySelector(`.G${count}`);
         // console.log(curclass);

         Gname = Gname.toLowerCase();
         finalinp = finalinp.toLowerCase();
         finalinpsize = finalinp.length;


         if (Gname == finalinp || Gname.slice(0, finalinpsize) == finalinp) {
             // console.log("yahooo");
             curclass.style.display = "";
         }
         // else if (Gname != finalinp) {
         //     console.log((Gname.slice(0, 2)));
         //     if ((Gname.slice(0, 2)).includes(finalinp)) {
         //         curclass.style.display = "";
         //     }
         //     else {
         //         curclass.style.display = "none";
         //     }
         // }
         else if((Gname.includes(finalinp))&&(finalinp.length>4)){
             curclass.style.display="";
         }
         else {
             // console.log("nopes");
             curclass.style.display = "none";
         }
         count++;
     });

 });