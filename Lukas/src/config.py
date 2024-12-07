from pathlib import Path
import torch

PROJECT_ROOT = Path(__file__).parent.parent
class Config:
    # Data paths relative to project root
    DATA_DIR = PROJECT_ROOT.parent / "data/mushroom_50k_v1"
    MODELS_DIR = PROJECT_ROOT / "models"
    CHECKPOINT_DIR = MODELS_DIR / "checkpoints"
    PLOTS_DIR = PROJECT_ROOT / "plots"
    INTERMEDIATE_DATA_DIR = PROJECT_ROOT.parent / "data/intermediate"
    
    # Create directories
    CHECKPOINT_DIR.mkdir(exist_ok=True)
    PLOTS_DIR.mkdir(exist_ok=True)
    INTERMEDIATE_DATA_DIR.mkdir(exist_ok=True, parents=True)
    
    # General settings
    SEED = 42
    MODEL_TYPE = "cnn"  # Options: "vgg" or "cnn"
    SAVE_CHECKPOINTS = False
    CHECKPOINT_FREQ = 5  # Save checkpoint every N epochs

    # Augmentation settings
    MAX_AUGMENTATION_FACTOR_PER_CLASS = 5
    AUGMENTATION_STEPS = {
        "rotation": True,
        "color_jitter": True,
        "affine": False
    }

    # Model parameters
    NUM_CLASSES = None  # Will be set dynamically based on dataset
    BATCH_SIZE = 32
    NUM_EPOCHS = 20
    
    # GPU settings
    DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # Learning rates
    VGG_LR = 3e-4
    CNN_LR = 1e-3
    WEIGHT_DECAY = 1e-4
    
    # Image parameters
    IMAGE_SIZE = 224  # input size of vgg19
    MEAN = [0.485, 0.456, 0.406]  # ImageNet normalization # TODO: Calculate mean and std from dataset
    STD = [0.229, 0.224, 0.225]
    
    # Logging settings
    LOG_LEVEL = "INFO"
    LOG_DIR = Path("logs")
    LOG_FORMAT = '[%(asctime)s] [%(levelname)-8s] --- %(message)s (%(filename)s:%(lineno)d)'
    

    # API settings    
    API_TITLE = "Mushroom API"
    API_VERSION = "0.1"
    API_DESCRIPTION = "API for mushroom species classification"
    HOST = "0.0.0.0"
    PORT = 5000

