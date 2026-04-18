namespace SampleApi.Models
{
    public class ExampleResponse
    {
        public bool Success { get; set; }
        public string Message { get; set; } = string.Empty;
        public DateTime ProcessedAt { get; set; }
    }

    public class HealthResponse
    {
        public string Status { get; set; } = string.Empty;
        public DateTime Time { get; set; }
    }
}
