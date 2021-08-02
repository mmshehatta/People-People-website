/************************** Actions ****************************/
// delete offer with reload
$("[data-delete]").on("click", function (e) {
  e.preventDefault();
  // var url=$(this).data('deleteaj');
  var url = $(this).attr("href");
  // var post=$(this).closest('.postContainer');
  var offer = $("#crardWraper");
  Swal.fire({
    title: "Are you sure to delete it ?",
    text: "if You delete can't return back !",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#d33",
    cancelButtonColor: "#3085d6",
    confirmButtonText: "Yes ، Delete it!",
    cancelButtonText: "Back",
  }).then(function (e) {
    if (e.value == true) {
      $.ajax({
        type: "GET",
        url: url,
        success: function () {
          offer.remove();
          Swal.fire("تم !", "offer deleted sucessfully!", "success");
          window.location.href = "http://127.0.0.1:8000/offers";
        },
      });
    }
  });
});

/************************** ************************************/
// [2] search on offer
//--------------------

// $("#user-input").on('focus',(e)=>{
//     window.location.href = "http://127.0.0.1:8000/search-page";
// })


$("#search-form").on("keydown", (e) => {
    // e.preventDefault()
  // window.location.href = "http://127.0.0.1:8000/search-page";
  // console.log(e.target.value)
  searchInput = $("#user-input");
  url = $("#search-form").attr("action");
  console.log(searchInput.val().length);
  //    var resultBox = $('res-row')
  var resultBox = document.getElementById("crardWraper-search");
  console.log("resltBox", resultBox);

  $.ajax({
    type: "GET",
    url: url,
    data: {
      offer: e.target.value,
    },
    success: function (res) {
      console.log("res", res.data);
      var data = res.data;
      if (Array.isArray(data)) {
        console.log("We have an array");
          data.forEach((offer) => {
          resultBox.innerHTML += `
                    <div class="card">
                      
                      <img
                        class="card-img-top"
                        src="media/${offer.image}"
                        height="235px"
                      />
          
                    
                      <div class="card-body">
                        <h5 class="card-title border-bottom pb-3 text-right text-success">
                         ${offer.owner}
                          <small
                            class="float-left d-inline-flex text-secondary"
                            style="font-size: 13px"
                          >
                            <i class="fa fa-clock m-1 text-success"></i>
                            ${offer.date}
                          </small>
                        </h5>
                        <p class="card-text text-left">
                         ${offer.name}
          
                        </p>
                        <hr>
                        <a href="http://127.0.0.1:8000/${offer.pk}" class="float-right text-success">
                          More
                          <i class="fas fa-angle-double-right"></i>
                        </a>
                        <a href="" class="float-left text-success">
                          Book Now <i class="fas fa-clipboard-check"></i>
                        </a>
          
                     
                        <a href="http://127.0.0.1:8000/${offer.pk}/update" class="text-primary ml-5">
                          <i class="fas fa-edit"></i>
                        </a>
                        <a data-delete  href="http://127.0.0.1:8000/${offer.pk}/delete" class="text-danger ml-5">
                          <i class="fas fa-minus-circle"></i></a>
                        
                          </div>
                    </div>
                  </div>
                 
               
                `;
        });
      } else {
        if (searchInput > 0) {
          resultBox.html(`${data}`);
        } else {
          console.log("d-block");
        }
      }
    },
    error: function (err) {
      console.log("err", err);
    },
  });
});

/**********************************************************************************/
//[1] add need
//------------
$("#link-take-offer").on("click", function (e) {
  e.preventDefault();
  object_id = $(this).attr("data-object-id");
  var offer_id = $(this).attr("data-object-id", object_id);
  // var offer = $(this).attr("data-object-id",offer_id);
  console.log("offer_id", offer_id);
  // console.log("offer" , offer);
  $.ajax({
    type: "GET",
    url: $(this).attr("href"),
    data: {
      // "csrfmiddlewaretoken":"{{ csrf_token }}",
      offer_id: offer_id,
    },
    success: function (respose) {
      if (respose == "success") {
        Swal.fire({
          position: "top-end",
          icon: "success",
          title: "تم حجز العرض بنجاح",
          showConfirmButton: false,
          timer: 1500,
        });
      } else {
        Swal.fire({
          position: "top-end",
          icon: "warning",
          title: "لقد قمت بحجز هذا العرض من قبل",
          showConfirmButton: false,
          timer: 1500,
        });
      }
    },
  });
});

// delete action without reload
//[2] delete need
//---------------
$("[need-data-delete]").on("click", function (e) {
  e.preventDefault();
  // var url=$(this).data('deleteaj');
  var url = $(this).attr("href");
  // var post=$(this).closest('.postContainer');
  var need = $("#needtrid");
  console.log("need", need);
  Swal.fire({
    title: "Are you sure to delete it ?",
    text: "if You delete can't return back !",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#d33",
    cancelButtonColor: "#3085d6",
    confirmButtonText: "Yes ، Delete it!",
    cancelButtonText: "Back",
  }).then(function (e) {
    if (e.value == true) {
      $.ajax({
        type: "GET",
        url: url,
        success: function () {
          need.remove();
          console.log("after remove");
          Swal.fire("تم !", "need deleted sucessfully!", "success");
          window.location.href = "http://127.0.0.1:8000/user-needs";
        },
      });
    }
  });
});

/*********************************************************************/

/************************** Effects ****************************/
/************************** ************************************/

$(".form").hide();

$(".show-hide-btn").click(function () {
  $(".form").toggle(1000);
});
