$(function() {
  $("#user_login").click(function() {
    $.ajax({
      url: "/user",
      data: $("form").serialize(),
      type: "POST",
      success: function(response) {
        console.log(response);
      },
      error: function(error) {
        console.log(error);
      }
    });
  });
});
