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
  Specification of a single field in an API model.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ApiFieldSpec extends NamedElement {

  private String fieldName;
  private String fieldType;
  private Boolean requiredField;
  private Boolean allowsNull;


}