using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using uaa.Models;

namespace uaa.Controllers;

public class APIController : Controller
{
    private readonly ILogger<APIController> _logger;

    public APIController(ILogger<APIController> logger)
    {
        _logger = logger;
    }

    public IActionResult Index()
    {
        return View();
    }

    [HttpPost]
    public JsonResult MultiSearch(string id, string offset, int titleChecked, int bodyChecked, int tagsChecked, int commentsChecked)
    {
        var query = "";

        if (titleChecked == 1){
            query += "title=" + id;
        } 

        if (bodyChecked == 1){
            if (titleChecked == 1){
                query += "&";
            }
            query += "body=" + id;
        } 

        if (tagsChecked == 1){
            if (titleChecked == 1 || bodyChecked == 1){
                query += "&";
            }
            query += "tags=" + id;
        } 

        if (commentsChecked == 1){
            if (titleChecked == 1 || bodyChecked == 1 || tagsChecked == 1){
                query += "&";
            }
            query += "comments=" + id;
        } 

        var client = new HttpClient();

        var webRequest = new HttpRequestMessage(HttpMethod.Get, "http://solr:8983/solr/gettingstarted/select?indent=true&start=" + offset + "&q.op=OR&q=*%3A*&" + query + "&useParams="){};
        
        var response = client.Send(webRequest);

        using var reader = new StreamReader(response.Content.ReadAsStream());
        
        dynamic jt = JsonConvert.DeserializeObject<dynamic>(reader.ReadToEnd());

        return Json(jt.response.docs);
    }

    [HttpPost]
    public JsonResult TitleSearch(string id, string offset)
    {
        var client = new HttpClient();

        var webRequest = new HttpRequestMessage(HttpMethod.Get, "http://solr:8983/solr/gettingstarted/select?indent=true&start=" + offset + "&q.op=OR&q=*%3A*&title=" + id + "&useParams="){};
        
        var response = client.Send(webRequest);

        using var reader = new StreamReader(response.Content.ReadAsStream());
        
        dynamic jt = JsonConvert.DeserializeObject<dynamic>(reader.ReadToEnd());

        return Json(jt.response.docs);
    }

    [HttpPost]
    public JsonResult BodySearch(string id, string offset)
    {
        var client = new HttpClient();

        var webRequest = new HttpRequestMessage(HttpMethod.Get,"http://solr:8983/solr/gettingstarted/select?indent=true&start=" + offset + "&q.op=OR&q=*%3A*&body=" + id + "&useParams="){};
        
        var response = client.Send(webRequest);

        using var reader = new StreamReader(response.Content.ReadAsStream());
        
        dynamic jt = JsonConvert.DeserializeObject<dynamic>(reader.ReadToEnd());

        return Json(jt.response.docs);
    }

    [HttpPost]
    public JsonResult TagsSearch(string id, string offset)
    {
        var client = new HttpClient();

        var webRequest = new HttpRequestMessage(HttpMethod.Get, "http://solr:8983/solr/gettingstarted/select?indent=true&start=" + offset + "&q.op=OR&q=*%3A*&tags=" + id + "&useParams="){};
        
        var response = client.Send(webRequest);

        using var reader = new StreamReader(response.Content.ReadAsStream());
        
        dynamic jt = JsonConvert.DeserializeObject<dynamic>(reader.ReadToEnd());

        return Json(jt.response.docs);
    }

    [HttpPost]
    public JsonResult CommentsSearch(string id, string offset)
    {
        var client = new HttpClient();

        var webRequest = new HttpRequestMessage(HttpMethod.Get, "http://solr:8983/solr/gettingstarted/select?indent=true&start=" + offset + "&q=*%3A*&title=" + id + "&useParams="){};
        
        var response = client.Send(webRequest);

        using var reader = new StreamReader(response.Content.ReadAsStream());
        
        dynamic jt = JsonConvert.DeserializeObject<dynamic>(reader.ReadToEnd());

        return Json(jt.response.docs);
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
