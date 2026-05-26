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
  Specification of a context implementation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ContextSpec extends ModelElement {

  private String contextLinearity;
  private Boolean storesComponentHistory;
  private Boolean acceptsMessageAttachments;


}