using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace Hangman.Models
{
    public class User
    {
        [Key]
        public int UserId { get; set; }

        [Required]
        public string Username { get; set; }

        [Required]
        public string Password { get; set; }

        [Required]
        public string Mail { get; set; }

        [Required]
        public bool IsAdmin { get; set; }

        public ICollection<WordApproval> WordApprovals { get; set; }

        public ICollection<WordInfo> Words { get; set; }

        public ICollection<Game> Games { get; set; }
    }
}
