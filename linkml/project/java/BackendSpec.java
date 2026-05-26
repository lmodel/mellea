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
  Specification of a Mellea backend implementation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BackendSpec extends ModelElement {

  private String backendFamily;
  private List<ModelIdentifierSpec> modelIdentifier;
  private FormatterSpec defaultFormatter;
  private List<String> modelOptionsKey;
  private Boolean supportsStreaming;
  private Boolean supportsToolCalls;
  private Boolean supportsMultimodal;


}