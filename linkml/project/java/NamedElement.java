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
  Abstract base for any named, identifiable schema element.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class NamedElement  {

  private URI id;
  private String name;
  private String description;
  private String modulePath;
  private String sourceFile;
  private String packageKind;
  private String elementKind;
  private List<String> coverageScope;
  private List<String> tags;


}