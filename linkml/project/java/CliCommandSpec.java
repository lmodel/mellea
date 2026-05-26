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
  Specification of a CLI command exposed under `m`.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CliCommandSpec extends ModelElement {

  private String commandGroup;
  private String commandPath;
  private String commandPurpose;
  private List<ApiModelSpec> inputModel;
  private List<ApiModelSpec> outputModel;


}