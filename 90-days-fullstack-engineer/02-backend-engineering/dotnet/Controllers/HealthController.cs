using Microsoft.AspNetCore.Mvc;
using SampleApi.Models;
using SampleApi.Services;

namespace SampleApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class HealthController : ControllerBase
    {
        private readonly IExampleService _exampleService;

        public HealthController(IExampleService exampleService)
        {
            _exampleService = exampleService;
        }

        [HttpGet]
        public ActionResult<HealthResponse> Get()
        {
            var result = _exampleService.GetHealthStatus();
            return Ok(result);
        }

        [HttpPost("check")]
        public ActionResult<ExampleResponse> Check([FromBody] ExampleRequest request)
        {
            var result = _exampleService.ProcessRequest(request);
            return Ok(result);
        }
    }
}
