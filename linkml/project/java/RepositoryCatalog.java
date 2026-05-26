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
  Top-level catalog rooting the analysed repository snapshot.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RepositoryCatalog extends NamedElement {

  private String repositoryRoot;
  private LocalDate analyzedOn;
  private List<String> includesPath;
  private List<String> excludesPath;
  private List<ModelElement> declaresElement;


}