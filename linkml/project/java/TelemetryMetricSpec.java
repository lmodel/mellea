package None;

/* metamodel_version: 1.11.0 */
/* version: 2026-05-26 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Specification of a telemetry metric emitted by Mellea.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TelemetryMetricSpec extends ModelElement {

  private List<String> metricName;


}