using SampleApi.Models;

namespace SampleApi.Services
{
    public class ExampleService : IExampleService
    {
        public HealthResponse GetHealthStatus()
        {
            return new HealthResponse { Status = "Healthy", Time = DateTime.UtcNow }; 
        }

        public ExampleResponse ProcessRequest(ExampleRequest request)
        {
            if (string.IsNullOrWhiteSpace(request.Text))
            {
                throw new ArgumentException("Text cannot be empty");
            }

            return new ExampleResponse
            {
                Success = true,
                Message = $"Processed instance {request.Id}",
                ProcessedAt = DateTime.UtcNow
            };
        }
    }
}
