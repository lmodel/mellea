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
  Specification of a method exposed by a runtime class.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MethodSpec extends NamedElement {

  private String methodName;
  private String methodSignature;
  private String lifecycleRole;


}