$(document).ready(function () {
  var current_fs, next_fs, previous_fs; //fieldsets
  var opacity;
  var current = 1;
  var steps = $("fieldset").length;
  var edu = $("#edu-form").html();
  var job = $("#job-form").html();
  var skill = $("#skill-form").html();

  setProgressBar(current);

  $(".next").click(function () {
    var chk = 0;
    var current_fs_id;
    current_fs = $(this).parent();
    current_fs_id = current_fs.attr("id");

    $("#" + current_fs_id + " input:required").each(function () {
      if ($(this).val() === "") chk = 0;
    });

    if (chk == 1) {
      Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "Fill all the fields",
      });
    } else {
      next_fs = $(this).parent().next();

      //Add Class Active
      $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

      //show the next fieldset
      next_fs.show();
      //hide the current fieldset with style
      current_fs.animate(
        { opacity: 0 },
        {
          step: function (now) {
            // for making fielset appear animation
            opacity = 1 - now;

            current_fs.css({
              display: "none",
              position: "relative",
            });
            next_fs.css({ opacity: opacity });
          },
          duration: 500,
        }
      );
      setProgressBar(++current);
    }
  });

  $(".previous").click(function () {
    current_fs = $(this).parent();
    previous_fs = $(this).parent().prev();

    //Remove class active
    $("#progressbar li")
      .eq($("fieldset").index(current_fs))
      .removeClass("active");

    //show the previous fieldset
    previous_fs.show();

    //hide the current fieldset with style
    current_fs.animate(
      { opacity: 0 },
      {
        step: function (now) {
          // for making fielset appear animation
          opacity = 1 - now;

          current_fs.css({
            display: "none",
            position: "relative",
          });
          previous_fs.css({ opacity: opacity });
        },
        duration: 500,
      }
    );
    setProgressBar(--current);
  });

  function setProgressBar(curStep) {
    var percent = parseFloat(100 / steps) * curStep;
    percent = percent.toFixed();
    $(".progress-bar").css("width", percent + "%");
  }

  function mapping(className) {
    var returnList = $("." + className)
      .map(function () {
        return this.value;
      })
      .get();
    return returnList;
  }
  const zip = (...arr) => {
    const zipped = [];
    arr.forEach((item, ind) => {
      item.forEach((i, index) => {
        if (!zipped[index]) {
          zipped[index] = [];
        }
        if (!zipped[index][ind]) {
          zipped[index][ind] = [];
        }
        zipped[index][ind] = i || "";
      });
    });
    return zipped;
  };

  function getZip(...classNames) {
    var arr = [];
    for (let i = 0; i < classNames.length; i++) {
      arr.push(mapping(classNames[i]));
    }
    return zip(...arr);
  }

  $("#submitBtn").click(function () {
    job = getZip(
      "job-title",
      "job-employer",
      "job-start_date",
      "job-end_date",
      "job-description"
    );

    education = getZip(
      "edu-degree",
      "edu-branch",
      "edu-university",
      "edu-passing_year",
      "edu-result"
    );

    skill = getZip("skill-title", "skill-level");
    $.ajax({
      type: "POST",
      url: "",
      data: {
        csrfmiddlewaretoken: csrftoken,
        education: JSON.stringify(education),
        job: JSON.stringify(job),
        skill: JSON.stringify(skill),
      },
      dataType: "json",
      success: function (response) {
      },
    });
  });
 

  $(".edu-addMore").click(function () {
    $("#edu-form").append(edu);

    $("#edu-form").load();
  });

  $(".job-addMore").click(function () {
    $("#job-form").append(job);

    $("#job-form").load();
  });
  $(".skill-addMore").click(function () {
    $("#skill-form").append(skill);

    $("#skill-form").load();
  });
});
