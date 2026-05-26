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
  Specification of a requirement validator.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RequirementSpec extends ModelElement {

  private String validationStyle;
  private Boolean mayTriggerRepair;


}