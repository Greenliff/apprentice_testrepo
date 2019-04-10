using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace Hangman.Models
{
    public class WordInfo
    {
        [Key]
        public int WordId { get; set; }

        [Required]
        public string Word { get; set; }

        [Required]
        public bool IsApproved { get; set; }

        [Required]
        public DateTime DateSubmitted { get; set; }

        [Required]
        public int SubmitterId { get; set; }

        public User Submitter { get; set; }

        [Required]
        public int LanguageId { get; set; }

        public Language Language { get; set; }

        public ICollection<WordInGame> WordInGames { get; set; }

        public ICollection<WordApproval> WordApprovals { get; set; }
    }
}
