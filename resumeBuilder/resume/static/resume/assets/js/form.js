$(document).ready(function () {
  var current_fs, next_fs, previous_fs; //fieldsets
  var opacity;
  var current = 1;
  var steps = $("fieldset").length;
  var edu = $("#edu-form").html();
  var job = $("#job-form").html();
  var skill = $("#skill-form").html();
  var skill_count = 1;
  var job_count = 1;
  var education_count = 1;

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

    info = getZip("info");

    $.ajax({
      type: "POST",
      url: "",
      data: {
        csrfmiddlewaretoken: csrftoken,
        education: JSON.stringify(education),
        job: JSON.stringify(job),
        skill: JSON.stringify(skill),
        info: JSON.stringify(info),
      },
      dataType: "json",
      success: function (response) {},
    });
  });

  

  

  function changeForm(idName, count) {
    $("#" + idName + "-1").attr("id", idName + "-0");
    $("#" + idName + "-1").attr("id", idName + "-" + String(count));
    $("#" + idName + "-0").attr("id", idName + "-1");
  }

  

  function changePreview(idName, count, templateId) {
    $("#" + templateId)
      .contents()
      .find("#"+ idName +"-1")
      .attr("id", idName+"-0");

    $("#" + templateId)
      .contents()
      .find("#"+idName+"-1")
      .attr("id", idName+"-" + String(count));

    $("#" + templateId)
      .contents()
      .find("#"+idName+"-0")
      .attr("id", idName+"-1");
  }

  

  $(".edu-addMore").click(function () {
    education_count++;
    $("#edu-form").append(edu);
    changeForm("education", education_count);
    changeForm("edu-del", education_count);
    changeForm("degree",education_count); 
    changeForm("branch",education_count); 
    changeForm("university",education_count); 
    changeForm("passing_year",education_count); 
    changeForm("result",education_count); 
    changeForm("edu-list",education_count);
    changeForm("edu-href", education_count);
    
    $("#edu-href-"+String(education_count)).attr('href', "#edu-list-"+String(education_count));
    var xyz = $("#degree-"+String(education_count-1)).val();
    // $("#edu-href-"+String(education_count-1)).html(xyz+' <i class="bx bx-chevron-down icon-show"></i><i class="bx bx-chevron-up icon-close"></i>');
    $("#edu-href-"+String(education_count)).html(xyz+' <i class="bx bx-chevron-down icon-show"></i><i class="bx bx-chevron-up icon-close"></i><div onclick="myFunctionElt(this);" id="edu-del-'+education_count+'">delete</div>');

    var new_edu = $("#template1").contents().find("#addneweducation").html();
    $("#template1").contents().find("#yui-u-2").append(new_edu);

    changePreview("degree",education_count,"template1"); 
    changePreview("branch",education_count,"template1"); 
    changePreview("university",education_count,"template1"); 
    changePreview("passing_year",education_count,"template1"); 
    changePreview("result",education_count,"template1"); 
    changePreview("education",education_count,"template1"); 
    $("#edu-form").load();
  });

  $(".job-addMore").click(function () {
    job_count++;
    $("#job-form").append(job);
    changeForm("job_title",job_count);
    changeForm("employer",job_count);
    changeForm("start_date",job_count);
    changeForm("end_date",job_count);
    changeForm("experience_description",job_count);


    var new_job = $("#template1").contents().find("#addnewjob").html();
    $("#template1").contents().find("#yui-u-1").append(new_job);
    
    
    changePreview("job_title",job_count,"template1");
    changePreview("employer",job_count,"template1");
    changePreview("start_date",job_count,"template1");
    changePreview("end_date",job_count,"template1");
    changePreview("experience_description",job_count,"template1");

    $("#job-form").load();
  });


  $(".skill-addMore").click(function () {
    skill_count++;
    $("#skill-form").append(skill);
    changeForm("skill_detail", skill_count);
    changeForm("skill_level", skill_count);

    var new_skill = $("#template1").contents().find("#addnewskill").html();
    $("#template1").contents().find("#yui-u").append(new_skill);
    changePreview("skill_detail",skill_count,"template1");
    changePreview("skill_level",skill_count,"template1");
    $("#skill-form").load();
  });
});
