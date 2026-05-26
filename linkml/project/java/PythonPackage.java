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
  A logical Python package (directory) inside the repository.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PythonPackage extends NamedElement {

  private String packageName;
  private List<PythonPackage> dependsOnPackage;
  private List<ModelElement> declaresElement;


}