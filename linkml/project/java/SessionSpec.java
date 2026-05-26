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
  Specification of a Mellea session.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SessionSpec extends ModelElement {

  private BackendSpec usesBackend;
  private ContextSpec usesContext;
  private List<MethodSpec> exposedMethod;


}