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
  Specification of a Mellea stdlib component type.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ComponentSpec extends ModelElement {

  private String componentCategory;
  private List<String> inputModality;
  private String parsedOutputType;


}