using SampleApi.Models;

namespace SampleApi.Services
{
    public interface IExampleService
    {
        HealthResponse GetHealthStatus();
        ExampleResponse ProcessRequest(ExampleRequest request);
    }
}
