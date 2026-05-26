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
  Cross-provider identifier table for a single model.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ModelIdentifierSpec extends NamedElement {

  private String hfModelName;
  private String ollamaName;
  private String watsonxName;
  private String openaiName;
  private String bedrockName;
  private List<String> providerName;


}