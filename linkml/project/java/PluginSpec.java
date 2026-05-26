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
  Specification of a Mellea plugin and the hooks it registers.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PluginSpec extends ModelElement {

  private String pluginMode;
  private List<String> hookType;
  private List<HookPayloadSpec> payloadModel;
  private Integer pluginPriority;


}