// Please see documentation at https://docs.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// Write your JavaScript code.

function setHtml(results) {
    $("#results").html("");
    console.log(results);
    for (var i = 0; i < results.length; i++) {
        var answer = results[i];
        console.log(answer);
        var curHtml = "<div class='card-panel white'>";
        curHtml += "<h4>" + answer["title"][0] + "</h4><br>";
        curHtml += "<p>" + answer["body"][0] + "</p><br>";
        if (answer["replies"] != undefined) {
            for (var ic = 0; ic < answer["replies"].length; ic++) {
                var comment = answer["replies"][ic];
                curHtml += "<div class='card-panel white'>";
                curHtml += comment;
                curHtml += "</div><br>";
            }
        }
        if (answer["tags"] != undefined) {
            for (var it = 0; it < answer["tags"].length; it++) {
                var tag = answer["tags"][it];
                curHtml += "<a href='/?tag=" + tag + "'>#" + tag + "</a>";
                if (it < (answer["tags"].length-1)){
                    curHtml += ", "
                }
            }
        }
        curHtml += "</div><br>";
        $("#results").append(curHtml);
    }
    $("#nextPage").attr("href", parseInt($("#nextPage").attr("href"))+10);
}
function getRequest() {
    var searchValue = $("#autocomplete-input").val();
    var titleChecked = $("#title").is(":checked");
    var bodyChecked = $("#body").is(":checked");
    var tagsChecked = $("#tags").is(":checked");
    var commentsChecked = $("#comments").is(":checked");
    + titleChecked;
    + bodyChecked;
    + tagsChecked;
    + commentsChecked;
    if ((titleChecked + bodyChecked + tagsChecked + commentsChecked) > 1) {
        $.post("/api/multisearch/", {
            id: searchValue, 
            offset: $("#nextPage").attr("href"),
            titleChecked: titleChecked,
            bodyChecked: bodyChecked,
            tagsChecked: tagsChecked,
            commentsChecked: commentsChecked
        }, function (data) {
            setHtml(data);
        });
    } else {
        if (titleChecked == 1) {
            $.post("/api/titlesearch/", { id: searchValue, offset: $("#nextPage").attr("href") }, function (data) {
                setHtml(data);
            });
        } else if (bodyChecked == 1) {
            $.post("/api/bodysearch/", { id: searchValue, offset: $("#nextPage").attr("href") }, function (data) {
                setHtml(data);
            });
        } else if (tagsChecked == 1) {
            $.post("/api/tagssearch/", { id: searchValue, offset: $("#nextPage").attr("href") }, function (data) {
                setHtml(data);
            });
        } else if (commentsChecked == 1) {
            $.post("/api/commentssearch/", { id: searchValue, offset: $("#nextPage").attr("href") }, function (data) {
                setHtml(data);
            });
        } else {
            $.post("/api/titlesearch/", { id: searchValue, offset: $("#nextPage").attr("href") }, function (data) {
                setHtml(data);
            });
        }
    }
}
$(document).ready(function () {
    let searchParams = new URLSearchParams(window.location.search);
    if (searchParams.has('tag')){
        let param = searchParams.get('tag');
        $("#autocomplete-input").val(param);
        $("#tags").prop( "checked", true );
    }
    $("#nextPage").click(function (e) {
        e.preventDefault();
        getRequest();
    });
    $("#searchForm").submit(function (e) {
        e.preventDefault();
        $("#nextPage").attr("href", 0);
        getRequest();
    });
});