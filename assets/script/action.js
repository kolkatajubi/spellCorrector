$(document).ready(function() {
  console.log("ready");
  $(".buttonBx").click(function(event) {
    console.log("ajax requesting....");
    $.ajax({
      type: "POST",
      url: "https://pixie.jubi.ai/spellCorrectorBackend/",
      data: JSON.stringify({ word: $("#input-field").val() }),
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      success: function(result) {
        console.log("success..");
        if (result.status === "success") {
          $("#score").text(result.score);
          $("#time").text(result.totalTime);
          $("#word").text(result["o/p word"]);
        }
      }
    });
  });
  $(".input-field").keypress(function(event) {
    if (event.keyCode === 13) {
      $(".buttonBx").click();
    }
  });
});
